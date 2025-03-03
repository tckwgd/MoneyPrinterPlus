#  Copyright © [2024] 程序那些事
#
#  All rights reserved.
#
#

import google.generativeai as genai
import streamlit as st

from config.config import my_config
from services.llm.llm_provider import LLMProvider


class MyGeminiService(LLMProvider):
    def __init__(self):
        super().__init__()
        # 从配置中获取 API 密钥
        api_key = my_config.get('llm', {}).get('gemini', {}).get('api_key', '')
        if not api_key:
            raise ValueError("Gemini API key not found in configuration")
        
        # 初始化 Gemini API
        genai.configure(api_key=api_key)
        
        # 设置提示模板
        self.topic_prompt_template = """
        请根据以下主题生成一段视频脚本内容：
        主题：{topic}
        语言：{language}
        长度：{length}字以内
        
        要求：
        1. 内容要生动有趣
        2. 适合短视频平台
        3. 语言要简洁明了
        4. 内容要有吸引力
        """
        
        self.keyword_prompt_template = """
        请根据以下内容提取5个关键词，用逗号分隔：
        {content}
        """
    
    def generate_content(self, content, prompt_template=None, language=None, length=None):
        """
        使用 Gemini 生成内容
        
        Args:
            content: 输入内容
            prompt_template: 提示模板
            language: 语言
            length: 内容长度
            
        Returns:
            生成的内容文本
        """
        if prompt_template:
            if language and length:
                prompt = prompt_template.format(topic=content, language=language, length=length)
            else:
                prompt = prompt_template.format(content=content)
        else:
            prompt = content
        
        # 调用 Gemini API
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        # 返回生成的内容
        return response.text 