from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, parsers

from .sample import iris_dataset, estimate
from .sample_data import dataset

# dataset = iris_dataset

def index(req):
    return render(req, "index.html")

class TrainingSetView(APIView):
    # parser_classes = (parsers.JSONParser,)

    def get(self, req):
        data = {
            "head":dataset["feature_names"],
            "data":dataset["data"],
            "target":dataset["target"],
            "targetNames":dataset["target_names"]
        }
        return Response(data)

class FitAndTransformView(APIView):
    parser_classes = (parsers.JSONParser,)

    def post(self, req):
        pred_result = estimate(req.data["trainingSet"], [req.data["labels"]])[0]
        return Response(pred_result)