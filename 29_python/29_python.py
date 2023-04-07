pattern= re.compile(r'^(?:0?[1-9]|[12][0-9]|3[01])/(?:0?[1-9]|1[0-2])/(?:19[0-9][0-9]|20[0-9][0-9]) ([0-1][0-9]|2[0-3]):([0-5][0-9]) Description: [a-zA-Z]+$')
# 24/02/2001 23:12 Description: need....
# yout message on 24 feb 2001 at 23:12 oc. can be write
#   your description : need
num = input('Enter data: ')
month = [' ','January','February','March','April','May','June','July','August','September','Octobre','November','December']

if pattern.findall(num):
    data = num.split('/')
    data = ' '.join(data).split(' ')


    print(f'your message on {data[0]} {month[int(data[1])]} {data[2]} at {data[3]}. can be written\nyour {data[4]} {data[5]}')