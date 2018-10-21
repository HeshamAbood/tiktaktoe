class Msisdn ():
    def __init__(self, msisdn):
        l=len(msisdn)
        if l==9:
            self.val=msisdn
        elif l==12:
            self.val=msisdn[3:]
        else:
            print ("WRONG MSISDN LENGTH")
            self.val=None

    def get_msisdn_cc(self):
        return "967"+str(self.val)
    
    def get_msisdn_val(self):
        return str(self.val)

    def __str__(self):
        return "967"+str(self.val)

    def get_del_record(self):
        del_rec="|2|{0}||||||0|0|||0|||||||||||||-1||||||96701|YE|".format(self.get_msisdn_cc())
        #print(del_rec)
        return del_rec