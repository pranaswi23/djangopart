from django.shortcuts import render

from django.http import HttpResponse

def fe (request):
    return HttpResponse('<h1> Age classification using speech processing </h1><form action="" methods=""><label for="name">Name*:</label> <input type="text" id="name" name=""size="50"></br></br><label for="email">Email Id*:</label> <input type="text" id="email" email=""size="50"></br></br><label for="phno">Mobile No*:</label> <input type="text" id="phno" phno=""size="20"></br></br><label for="file">Choose file to upload</label><input type="file" id="file" name="file" multiple></br></br><input type="submit" value="Submit"></br></br><label for="output">Output:</label> <input type="text" id="output" output=""size="20"></form>')

# Create your views here.
