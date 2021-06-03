import json

from flask import request


def create_api(app, poie_service):
    @app.route('/api/poie', methods=['POST'])
    def analysis():

        file = request.files["file"]
        if file is None:
            return "전송된 file을 찾을 수 없습니다.", 404

        print("content-type : " + str(file.content_type))
        # if file.content_type is None:
        #     return "File is empty", 400

        file_extension = (file.filename.split('.')[1])
        if file_extension != 'wav':
            return "오디오 파일은 wav 형식만 지원됩니다.", 400

        result = poie_service.analysis_audio(file)

        return json.dumps(result), 200
