url = 'http://www.google.co.uk'
url2 = "http://github.com/carbonfive/raygun"
url3 = "http://www.zombie-bites.com"
url4 = 'http://google.co.uk'


def domain_name(url):
    url = url.split('.')
    split = []
    for part in url:
        for word in part.split('/'):
            if word == 'com':
                break
            split.append(word)

    return split[-1]

def domain_name2(url):
    final = url.split('//')[-1]
    final = final.split('.')
    if final[0] != 'www':
        return final[0]
    else:
        return final[1]



def one(number):
    one = ['one', 'two', 'three', 'four', 'five','six','seven','eight','nine']
    return one[number-1]

def one_first(number):
    one_first = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifthteen', 'sixteen','seventeen','eighteen','nineteen']
    return one_first[number]
    
def two(number):
    two = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    return two[number-2]

def number2words(number):
    # count, or len of number
    read = str(number)
    length = len(read)

    if number == 0:
        return 'zero'
    
    if length == 1:
        return one(number)
    elif length == 2:
        if read[0] == '1': # if a one a different case
            return one_first(int(read[1]))
        else:
            if read[1] != '0':
                return two(int(read[0])) + '-' + one( int( read[1] ) )
            else:
                return two(int(read[0])) 

    elif length == 3:
        part1 = one(int(read[0]))
        part2 = number2words( int( read.replace(read[0], '', 1) ) )

        if not part2:
            return part1+ ' hundred'
        return part1 + ' hundred ' + part2

    elif length == 4:
        part1 = one(int(read[0]))
        part2 = number2words( int( read.replace(read[0], '', 1) ) )

        if not part2:
            return part1+ ' thousand'
        return part1 + ' thousand ' + part2
    
    elif 4 <= length <= 6 :
        #divide into two
        part1 = number2words( int( read[:7-len(read)] ) )
        part2 = number2words( int( read[7-len(read):] ) )
        if part2 == '':
            return part1 + ' thousand'
        return part1 + ' thousand ' + part2
    else:
        return ''


















