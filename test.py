# print(type({}) is list or type({}) is dict)
import re
import validators

st = "16.182.16.160:32000/gcr.io/kubebuilder/kube-rbac-proxy:v0.8.0"
print(validators.url(st))
if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{4,5}', st) != None:
    print("yes")
else:
    print("no")