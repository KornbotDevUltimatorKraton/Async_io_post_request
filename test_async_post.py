from flask import Flask,render_template,url_for,redirect,url_for,request,jsonify

app = Flask(__name__)


@app.route("/post_data",methods=['GET','POST'])
def get_endpoit_post():
         req_post = request.get_json(force=True)

         print(req_post)
         return jsonify(req_post)

if __name__ == "__main__":

       app.run(debug=True,host="0.0.0.0",port=5869)
