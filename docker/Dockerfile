# Note:
#   This DockerFile was created for MoneyPrinterPlus v4.7 with the aim of reducing usage costs and hoping that more people can experience its charm.
#   Human civilization is the development of productive forces guided by production tools, and we hope that this tool can contribute a little bit to human civilization.
#   If you have any questions, please feel free to contact the author or me.
#                                                   Email: fengapi@gmail.com
#
FROM python:3.12-slim

WORKDIR /app

# 复制项目文件
COPY . .

# 安装依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    portaudio19-dev \
    libgtk-3-dev \
    git && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8501

# 启动应用
CMD ["streamlit", "run", "gui.py", "--server.port=8501", "--server.address=0.0.0.0"]
