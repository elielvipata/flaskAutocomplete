from flask import Flask, request, render_template
  
  
app = Flask(__name__)
  
  
@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "GET":
		file = open("words", "r")
		lines = file.readlines()
		words = []
		for line in lines:
        		words.append(line[0:-1])
	return render_template("index.html", words=words)
  
  
if __name__ == '__main__':
	app.run(debug=True)
