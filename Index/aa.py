class ListNode :
    def __init__(self,w,docslist) :

        self.word = w
        self.docslist = []
        self.docslist.append(docslist)

TextIndex = []

def Search(word,TextIndex) :

    for i in TextIndex :
        if i.word == word :
            return TextIndex.index(i)   
        else :
            continue

    return -1


def Create(docs) :
    for d in docs :
        words = []
        for line in d :
            line = line.split()
            for word in line :
                if word not in words :
                    words.append(word)

            for word in words :

                node = ListNode(word,d.name)

                j = Search(word,TextIndex)

                if j == -1 :
                    TextIndex.append(node)

                else :
                    TextIndex[j].docslist.append(d.name)

def Display() :
    TextIndex.sort(key=lambda x: x.word, reverse=False)
    for i in TextIndex :
        print (i.word,i.docslist)


def main() :

    try :
        with open(r"1.txt") as a, open(r"2.txt") as b,       open(r"3.txt") as c :
        	docs = [a,b,c]  
        	Create(docs)
        Display()


    except IOError as e :
        print ('Operation Failed: %e' %e.strerror)

if __name__ == '__main__':
    main()
