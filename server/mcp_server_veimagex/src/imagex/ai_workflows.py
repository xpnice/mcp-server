import json
from abc import ABC, abstractmethod
from typing import Dict, Any, Callable

class AIWorkflowContext:
    def __init__(self, 
                 api: Any, 
                 service_id: str, 
                 tos_prefix_manager: Callable[[str], str],
                 creative_flow_id_getter: Callable[[], str]):
        self.api = api
        self.service_id = service_id
        self.tos_prefix_manager = tos_prefix_manager
        self.get_creative_flow_id = creative_flow_id_getter

    def get_tos_prefix(self) -> str:
        return self.tos_prefix_manager(self.service_id)

class WorkflowHandler(ABC):
    def __init__(self, name: str, template_id: str, description: str):
        self.name = name
        self.template_id = template_id
        self.description = description

    @property
    @abstractmethod
    def params_doc(self) -> str:
        pass

    @property
    @abstractmethod
    def default_params(self) -> Dict[str, Any]:
        pass

    @property
    def param_key(self) -> str:
        return ""

    def validate_and_merge_params(self, user_params: Dict[str, Any], context: AIWorkflowContext) -> Dict[str, Any]:
        merged = self.default_params.copy()
        for k, v in self.default_params.items():
            if k in user_params:
                merged[k] = user_params[k]
        return merged

    def process(self, input_key: str, data_type: str, user_params: Dict[str, Any], context: AIWorkflowContext) -> Dict[str, Any]:
        merged_params = self.validate_and_merge_params(user_params, context)
        wp = {
            "Input": {
                "ObjectKey": input_key,
                "DataType": data_type
            }
        }
        if self.param_key:
            wp[self.param_key] = merged_params

        return context.api.post_ai_process({
            "ServiceId": context.service_id,
            "WorkflowTemplateId": self.template_id,
            "WorkflowParameter": json.dumps(wp)
        })

class GenericHandler(WorkflowHandler):
    def __init__(self, name, template_id, description, param_key, defaults, doc_str):
        super().__init__(name, template_id, description)
        self._param_key = param_key
        self._defaults = defaults
        self._doc_str = doc_str

    @property
    def params_doc(self) -> str:
        return self._doc_str

    @property
    def default_params(self) -> Dict[str, Any]:
        return self._defaults

    @property
    def param_key(self) -> str:
        return self._param_key

class RemoveBgHandler(GenericHandler):
    def validate_and_merge_params(self, user_params: Dict[str, Any], context: AIWorkflowContext) -> Dict[str, Any]:
        merged = self.default_params.copy()
        for k, v in self.default_params.items():
            if k == "Contour" and "Contour" in user_params:
                d_c = v
                u_c = user_params["Contour"]
                if isinstance(u_c, dict):
                    merged_contour = d_c.copy()
                    merged_contour.update(u_c)
                    merged[k] = merged_contour
                else:
                    merged[k] = u_c
            else:
                merged[k] = user_params.get(k, v)
        return merged

class ProductCreativeHandler(WorkflowHandler):
    def __init__(self):
        super().__init__(
            name="product_creative", 
            template_id="system_workflow_product_img",
            description="E-commerce Creative Generation"
        )

    @property
    def params_doc(self) -> str:
        return """            - product_creative (Product Image Gen):
                       - CreativeFlowId (str, Required): The ID of the creative flow.
                       - Version (str, default "1.0"): "1.0" or "2.0".
                       - PositivePrompt (str, Required for v2): Prompt text (English for v1, En/Zh for v2).
                       - ImageRefKey (str, Required for v2): Background reference image URI/URL.
                       - ImageRefType (str, default "uri"): Type of reference image ("uri" or "url").
                       - OutputWidth/Height (int, default 800): [512, 1024].
                       - BatchSize (int, default 4): [1, 4].
                       - ProductRatio (float, default 0.6): (0, 1) e.g., 0.6.
                       - IpAdapterScale (float, default 0.9): [0, 1] (v2 only).
                       - CX/CY (int, default -1): Product center coordinates (v2 only, -1=center).
                       - Scene (str, default "general"): Background template (v1 only).
                         Options:
                         - general: 通用 (General)
                         - natural_pasture: 乡村牧场 (Natural Pasture)
                         - exhibit_home: 家居桌面 (Home Desktop)
                         - exhibit_simple: 极简展台 (Simple Stand)
                         - exhibit_kitchen: 厨房餐桌 (Kitchen Table)
                         - exhibit_bathroom: 洗漱桌面 (Bathroom Desktop)
                         - water_reflect: 水面光影 (Water Reflection)
                         - water_plants: 水面植物 (Water Plants)
                         - exhibit_light: 纯色光影 (Solid Light)
                         - water_ripples: 水面波纹 (Water Ripples)
                         - exhibit_luxury: 奢华展台 (Luxury Stand)
                         - exhibit_modern: 现代风景台 (Modern Stand)
                         - exhibit_stone: 植物岩石展台 (Stone Stand)
                         - exhibit_forest: 森林植物 (Forest Plants)
                         - exhibit_floor: 家居地面 (Home Floor)
                         - exhibit_toy: 玩具展台 (Toy Stand)
                         - exhibit_liquor: 洋酒展台 (Liquor Stand)
                         - exhibit_wine: 葡萄酒展台 (Wine Stand)
                         - exhibit_beer: 其他酒类展台 (Beer Stand)
                         - glisten_dew: 光台凝露 (Glistening Dew)
                         - spring_rock: 晶屿谧芳 (Spring Rock)
                         - dawn_silk: 雾纱晨礼 (Dawn Silk)
                         - flower_rock: 粉屿谧绽 (Flower Rock)
                         - origem_drop: 露屿青珀 (Origem Drop)
                         - sunrise_bake: 椰芝晨光 (Sunrise Bake)
                         - sea_crunch: 浪味鲜踪 (Sea Crunch)
                         - onyx_flow: 墨带智音 (Onyx Flow)
                         - joy_pack: 粉樱密语 (Joy Pack)
                         - drug_moss: 苔蕴健萃 (Drug Moss)
                         - toy_mat: 萌玩倚毯 (Toy Mat)
                         - coast_nut: 碧海果语 (Coast Nut)"""

    @property
    def default_params(self) -> Dict[str, Any]:
        return {
            "CreativeFlowId": None, "Version": "1.0", "PositivePrompt": None,
            "OutputWidth": 800, "OutputHeight": 800, "BatchSize": 4, "ProductRatio": 0.6,
            "Scene": "general", "IpAdapterScale": 0.9, "CX": -1, "CY": -1,
            "ImageRefType": "uri", "ImageRefKey": None, "EnableEnhance": False, "EnhanceMode": 0
        }

    def process(self, input_key: str, data_type: str, user_params: Dict[str, Any], context: AIWorkflowContext) -> Dict[str, Any]:
        merged = self.validate_and_merge_params(user_params, context)
        
        # Check params first, then environment
        final_flow_id = merged.get("CreativeFlowId")
        if not final_flow_id:
            final_flow_id = context.get_creative_flow_id()

        if not final_flow_id:
            raise ValueError("CreativeFlowId is required for product_creative (param or env var)")

        wp = {
            "Input": {"ObjectKey": input_key, "DataType": data_type},
            "CreativeFlowId": final_flow_id,
            "ProductAIGCType": "image",
            "Version": merged["Version"]
        }

        product_aigc = {
            "PositivePrompt": merged["PositivePrompt"],
            "OutputHeight": merged["OutputHeight"],
            "OutputWidth": merged["OutputWidth"],
            "BatchSize": merged["BatchSize"],
            "ProductRatio": merged["ProductRatio"]
        }

        if wp["Version"] == "2.0":
            if not product_aigc["PositivePrompt"]:
                raise ValueError("PositivePrompt is required for product_creative version 2.0")
            
            product_aigc["IpAdapterScale"] = merged["IpAdapterScale"]
            product_aigc["CX"] = merged["CX"]
            product_aigc["CY"] = merged["CY"]
            product_aigc["ImageRefType"] = merged["ImageRefType"]
            
            if not merged.get("ImageRefKey"):
                raise ValueError("ImageRefKey is required for product_creative version 2.0")
            
            ref_key = merged["ImageRefKey"]
            prefix = context.get_tos_prefix()
            if prefix and ref_key.startswith(prefix):
                ref_key = ref_key[len(prefix):].lstrip('/')
            product_aigc["ImageRefKey"] = ref_key
        else:
            product_aigc["Scene"] = merged["Scene"]

        wp["ProductAIGC"] = product_aigc

        if merged.get("EnableEnhance"):
            wp["ComprehensiveEnhance"] = {
                "Enable": True,
                "Mode": merged.get("EnhanceMode", 0)
            }

        return context.api.post_ai_process({
            "ServiceId": context.service_id,
            "WorkflowTemplateId": self.template_id,
            "WorkflowParameter": json.dumps(wp)
        })

class SeedreamHandler(GenericHandler):
    def validate_and_merge_params(self, user_params: Dict[str, Any], context: AIWorkflowContext) -> Dict[str, Any]:
        merged = super().validate_and_merge_params(user_params, context)
        if not merged.get("Prompt"):
            raise ValueError("Prompt is required for seedream")
        return merged

class AigcSrHandler(GenericHandler):
    def validate_and_merge_params(self, user_params: Dict[str, Any], context: AIWorkflowContext) -> Dict[str, Any]:
        merged = super().validate_and_merge_params(user_params, context)
        if "TargetWidth" in user_params: merged["TargetWidth"] = user_params["TargetWidth"]
        if "TargetHeight" in user_params: merged["TargetHeight"] = user_params["TargetHeight"]
        return merged

# Define all handlers
ALL_HANDLERS = {
    "cloud_sr": GenericHandler(
        name="cloud_sr",
        template_id="system_workflow_sr",
        description="Cloud Super Resolution (2-8x zoom).",
        param_key="SrParam",
        defaults={
            "Mode": 0, "Multiple": 2.0, "ShortMin": 16, "ShortMax": 1440,
            "LongMin": 16, "LongMax": 2160, "Policy": 0, "SharpRatio": 1.0, "DenoiseRatio": 0.7
        },
        doc_str="""            - cloud_sr (Cloud Super Res):
                       - Multiple (float, default 2.0): Scale factor [1.0-8.0].
                          * Note: If Mode=2, range is restricted to [1.0-2.0].
                       - Mode (int, default 0): 0=Enhance(Cartoon/Blur), 1=SR4x0(General), 2=VR, 3=SR4x3(General/Better).
                       - ShortMin (int, default 16): Min short edge [16, 1440].
                       - ShortMax (int, default 1440): Max short edge [16, 1440].
                       - LongMin (int, default 16): Min long edge [16, 2160].
                       - LongMax (int, default 2160): Max long edge [16, 2160].
                       - Policy (int, default 0): 0=Or(Short|Long match), 1=And(Short&Long match).
                       - SharpRatio (float, default 1.0): Sharpening intensity [0.0-1.0] (Mode 2 only).
                       - DenoiseRatio (float, default 0.7): Denoising intensity [0.0-1.0] (Mode 2 only)."""
    ),
    "smart_expansion": GenericHandler(
        name="smart_expansion",
        template_id="system_workflow_ai_bgfill",
        description="Intelligent Image Extension (outpainting).",
        param_key="BgfillParam",
        defaults={"Model": 3, "Top": 0.1, "Bottom": 0.1, "Left": 0.1, "Right": 0.1},
        doc_str="""            - smart_expansion (Outpainting):
                       - Model (int, default 3): 0=Cartoon, 1=General, 2=Product, 3=Intelligent 2.0(Recommended).
                       - Top/Bottom/Left/Right (float, default 0.1): Expansion ratio [0.0-0.4]."""
    ),
    "aigc_sr": AigcSrHandler(
        name="aigc_sr",
        template_id="system_workflow_ai_super_resolution",
        description="AIGC Super Resolution (detail enhancement).",
        param_key="GenDREnhanceParam",
        defaults={"ModelId": "ai_sr_model_v2", "Multiple": 2.0},
        doc_str="""            - aigc_sr (AIGC Super Res):
                       - Multiple (float, default 2.0): Scale factor (Max 30).
                       - ModelId (str, default "ai_sr_model_v2"): "ai_sr_model_v2" (GDR1.2).
                       - TargetWidth/Height (int, optional): Output dimensions (Max 10240)."""
    ),
    "translate": GenericHandler(
        name="translate",
        template_id="system_workflow_image_translate",
        description="Image Text Translation.",
        param_key="TranslateParam",
        defaults={"ModelId": "seed-translation", "SourceLang": "zh", "TargetLang": "en", "OutputFormat": "png"},
        doc_str="""            - translate (Image Translation):
                       - SourceLang (str, default "zh"): Source language code.
                         Options: 
                         - ar: Arabic (阿拉伯语), fr: French (法语), en: English (英语)
                         - ca: Catalan (加泰罗尼亚语), pt: Portuguese (葡萄牙语), es: Spanish (西班牙语)
                         - nl: Dutch (荷兰语), de: German (德语), sl: Slovenian (斯洛文尼亚语)
                         - az: Azerbaijani (阿塞拜疆语), bn: Bengali (孟加拉语), ru: Russian (俄语)
                         - no: Norwegian (挪威语), ms: Malay (马来语), zh: Chinese (中文)
                         - zh_hant: Chinese Traditional (中文繁体), cs: Czech (捷克语), sk: Slovak (斯洛伐克语)
                         - pl: Polish (波兰语), hu: Hungarian (匈牙利语), vi: Vietnamese (越南语)
                         - da: Danish (丹麦语), fi: Finnish (芬兰语), sv: Swedish (瑞典语)
                         - id: Indonesian (印尼语), he: Hebrew (希伯来语), it: Italian (意大利语)
                         - ja: Japanese (日语), ko: Korean (韩语), ta: Tamil (泰米尔语)
                         - th: Thai (泰语), tr: Turkish (土耳其语)
                       - TargetLang (str, default "en"): Target language code.
                         Options: 
                         - zh: Chinese (中文), zh_hant: Chinese Traditional (中文繁体)
                         - en: English (英语), ja: Japanese (日语), ko: Korean (韩语)
                         - ar: Arabic (阿拉伯语), pt: Portuguese (葡萄牙语), fr: French (法语)
                         - de: German (德语), es: Spanish (西班牙语), id: Indonesian (印尼语)
                         - it: Italian (意大利语), ms: Malay (马来语), ru: Russian (俄语)
                         - th: Thai (泰语), vi: Vietnamese (越南语)
                       - OutputFormat (str, default "png"): "png", "jpg", "jpeg", "webp"."""
    ),
    "quality_assessment": GenericHandler(
        name="quality_assessment",
        template_id="system_workflow_image_quality_evaluate",
        description="Large Model Image Quality Assessment.",
        param_key="QualityEvaluateParam",
        defaults={"ModelId": "default", "PromptId": "default", "MediaType": "image"},
        doc_str="""            - quality_assessment (Quality Evaluate):
                       - No specific required parameters. Automatically uses ModelId="default", PromptId="default"."""
    ),
    "product_creative": ProductCreativeHandler(),
    "remove_text": GenericHandler(
        name="remove_text",
        template_id="system_workflow_ai_workflow_psoriasis",
        description="E-commerce Text Removal.",
        param_key="AiWorkflowParam",
        defaults={"ModelId": "default"},
        doc_str="""            - remove_text (Text Removal):
                       - ModelId (str, default "default"): Fixed value."""
    ),
    "ocr": GenericHandler(
        name="ocr",
        template_id="system_workflow_image_ocr",
        description="Optical Character Recognition.",
        param_key="OCRParam",
        defaults={"ModelId": "default", "Scene": "general"},
        doc_str="""            - ocr (Optical Character Recognition):
                       - ModelId (str, default "default"): Fixed value.
                       - Scene (str, default "general"): "general" (通用), "license" (营业执照)."""
    ),
    "remove_bg": RemoveBgHandler(
        name="remove_bg",
        template_id="system_workflow_image_segment",
        description="Smart Background Removal.",
        param_key="SegmentParam",
        defaults={
            "ModelId": "general", "Refine": False,
            "Contour": {"Color": "#FFFFFF", "Size": 10},
            "TransBg": False, "OutFormat": "png"
        },
        doc_str="""            - remove_bg (Smart Background Removal):
                       - ModelId (str, default "general"): 
                         Options: "general" (v1), "human" (v1), "product" (v1), "humanv2" (v2), "productv2" (v2).
                       - Refine (bool, default false): Edge refinement (for v1 models).
                       - Contour (dict): {"Color": "#FFFFFF", "Size": 10} (for v2 models).
                       - TransBg (bool, default false): Transparent background crop (for v2 models).
                       - OutFormat (str, default "png"): "png", "jpeg", "webp"."""
    ),
    "seedream": SeedreamHandler(
        name="seedream",
        template_id="system_workflow_ark_seedream",
        description="ImageX-SeeDream Generation.",
        param_key="ArkSeedreamParam",
        defaults={
            "ModelId": "seedream4", "Prompt": None, "Size": "2048x2048", "Watermark": True,
            "EnableImageConversion": False, "SequentialImageGeneration": "disabled",
            "OptimizePromptOptions": {"Mode": "standard"}
        },
        doc_str="""            - seedream (SeeDream Generation):
                        - Prompt (str, Required): Description (max 300 zh/600 en chars).
                        - ModelId (str, default "seedream4"): Fixed value.
                        - Size (str, default "2048x2048"): "1K", "2K", "4K" or "WxH" (e.g. "1280x720").
                        - Watermark (bool, default true): Add "AI Generated" watermark.
                        - EnableImageConversion (bool, default false): Convert ref image if needed.
                        - SequentialImageGeneration (str, default "disabled"): "auto", "disabled".
                        - OptimizePromptOptions (dict): {"Mode": "standard"|"fast"}."""
    )
}
