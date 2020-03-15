
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def main():

    strTable = "<html><table><tr><th>Char</th><th>ASCII</th></tr>"

    for num in range(33,48):
     symb = chr(num)
     strRW = "<tr><td>"+str(symb)+ "</td><td>"+str(num)+"</td></tr>"
     strTable = strTable+strRW

    strTable = strTable+"</table></html>"
    return(strTable)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
