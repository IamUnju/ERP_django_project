from datetime import datetime
from apps.products.models.ProductGrnModel import ProductsGRN_hdr

class Reference_number:
    def __init__(self,ref_no):
        self.ref_no = ref_no
    @staticmethod
    def Reference_no_generator(grn):
          
        year = datetime.now().year
        
        latest_grn = ProductsGRN_hdr.objects.filter(grn_ref_no__startswith="GRN").order_by("sno").last()
    
        if latest_grn:
            print(latest_grn.grn_ref_no)
            last_number = int(latest_grn.grn_ref_no.split("-")[-1])
            new_number = last_number + 1
            print(new_number)
        else:
            new_number = 1  
        new_grn = f"GRN-{year}-{new_number}"
        return new_grn    
             
        
    
        