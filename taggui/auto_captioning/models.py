from auto_captioning.enums import ModelType

MODELS = [
    'internlm/internlm-xcomposer2-vl-7b-4bit',
    'internlm/internlm-xcomposer2-vl-7b',
    'THUDM/cogagent-vqa-hf',
    'THUDM/cogvlm-chat-hf',
    'vikhyatk/moondream2',
    'vikhyatk/moondream1',
    'llava-hf/llava-1.5-7b-hf',
    'llava-hf/llava-1.5-13b-hf',
    'llava-hf/bakLlava-v1-hf',
    'Salesforce/instructblip-vicuna-7b',
    'Salesforce/instructblip-vicuna-13b',
    'Salesforce/instructblip-flan-t5-xl',
    'Salesforce/instructblip-flan-t5-xxl',
    'Salesforce/blip2-opt-2.7b',
    'Salesforce/blip2-opt-6.7b',
    'Salesforce/blip2-opt-6.7b-coco',
    'Salesforce/blip2-flan-t5-xl',
    'Salesforce/blip2-flan-t5-xxl',
    'microsoft/kosmos-2-patch14-224'
]


def get_model_type(model_id: str) -> ModelType:
    if 'cogagent' in model_id.lower():
        return ModelType.COGAGENT
    if 'cogvlm' in model_id.lower():
        return ModelType.COGVLM
    if 'kosmos' in model_id.lower():
        return ModelType.KOSMOS
    if 'llava' in model_id.lower():
        return ModelType.LLAVA
    if 'moondream' in model_id.lower():
        return ModelType.MOONDREAM
    if 'xcomposer2' in model_id.lower():
        return ModelType.XCOMPOSER2
    return ModelType.OTHER
