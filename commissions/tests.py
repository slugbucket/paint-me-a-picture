from django.test import TestCase
import datetime

from django.utils import timezone

from .models import Commission, Enquiry

# Create your tests here.
class CommissionMethodTests(TestCase):

    def createCommission(self):
        """
        """
        #cty = CommissionType(id = 1, name = "Oil")
        #enq = Enquiry(id = 1, title = 'Oil Portrait', fullnme = "Bob Tester", contact_address = "bob@testzone.net", commission_type_id = 1, due_date = "2017-12-12")
        cmn = Commission(enquiry_id = 1, commission_type = 1)
        print("createCommissionTest.")
        self.assertIs(cmn.enquiry.title == "Oil Portrait", True)
