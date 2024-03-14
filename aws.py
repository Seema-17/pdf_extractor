from addressExt import get_address
from delta  import get_data


filenames=["AmazonWebServices","AmazonWebServices-2","AmazonWebServices3" ]
for file in filenames:
    get_address('./tests/input/'+file + ".pdf")
    print("**********************************************")
    get_data('./tests/output/'+file + ".json")
    print("#########################################################################################")
