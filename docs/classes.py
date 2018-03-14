class store(object):
    bankrupt = False
    def sum(self, a, b):
        c = a+b
        return c
    def am_i_bankrupt(self):
        return self.bankrupt

gio = store()
dan = store()
gio.bankrupt = False
gio.sum(1,2)
gio.am_i_bankrupt()
dan.sum(3,4)
dan.am_i_bankrupt()
gio.bankrupt = True
gio.am_i_bankrupt()
dan.am_i_bankrupt()
