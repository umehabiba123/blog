from django.shortcuts import HttpResponse
class middleWareclas:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print("this is before view")
        response = self.get_response(request)
        print("this is after view")
        return response
    # def process_view(request,*arg,**kwr):
    #     print("process view")
    #     return HttpResponse("This run the process view")
    def process_exception(self,request,exception):
        msg = exception
        cla = exception.__class__.__name__
        print(cla)
        return HttpResponse(msg)
    