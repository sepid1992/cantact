from django.shortcuts import render
def home(request):
    return render(request,"information_app/home.html")

def contact(request):
    contact_info = {
        {'section': 'Fani','phone': '038-32226200','website': 'https://http://portal.ctvto.ir/',
            'address': 'شهرکرد بلوار انقلاب جنب پل هوایی ، اداره کل آموزش فنی و حرفه ای استان'},
       
        {'section': 'Uni','phone': '038-32324407','website': 'https://sku.ac.ir/',
            'address': 'شهرکرد- بلوار رهبر- دانشگاه شهرکرد'},
        
        {'section': 'Jobs','phone': '038-32224858','website': 'http://chmb.mcls.gov.ir/',
            'address': 'شهرکرد- خیابان پیروزی- مجتمع ادارات ستاد'},
        
        {'section': 'Tamin','phone': '038-32263301','website': 'https://chb.tamin.ir/',
            'address': 'شهرکرد، خیابان شهیدبهشتی، ک 45 '},
        
    }
    return render(request, 'phonebook/contact.html', {'contact_info': contact_info})
   