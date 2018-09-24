# -*- coding: utf-8 -*-
from locators import *
import fronttests as r
import time

passed_test_count = 0
failed_test_count = 0

# Tests with parametrs
test_registration = r.Registration('tester', 'testoviy', regmail, 'qwe123QWE')
test_authorization = r.Authorization('tester@storiqa.com', 'qwe123QWE')
test_user_profile = r.User()
test_create_store = r.Store(regname, regname, 333, unic)
test_buy_item = r.Checkout(product)

# test_suite = [test_authorization.start(), test_create_store.create()]
test_suite = [test_authorization.start(), test_user_profile.profile(),
              test_user_profile.adress_add(), test_user_profile.adress_del(),
              test_create_store.edit()]

if __name__ == "__main__":

    for i in test_suite:
        if i is True:
            passed_test_count += 1
        else:
            failed_test_count += 1
    print ('Test finished with %s PASSED and %s FAILED' % (passed_test_count, failed_test_count))
    if failed_test_count > 0:
        raise r.TestFailException()

   # input('END')