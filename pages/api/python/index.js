let {PythonShell} = require('python-shell')

const PDFDocument = require('pdfkit');
const doc = new PDFDocument({size: 'A7'});

const data = [{"q1":1},{"q2":2}]





export default function handler(req, res) {

    PythonShell.run('./pages/api/python/test.py').then(async (messages)=> {
        // results is an array consisting of messages collected during execution
        console.log('results: %j', messages[0]);
        res.send({message:"funciona"})
        return
      });

  
      
  }
