# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StatusCode(models.Model):
    status_name = models.CharField(max_length=20)
    status_desc = models.CharField(max_length=40)
    is_active = models.BooleanField()

    class Meta:
        abstract = True


class LabelCode(models.Model):
    label_name = models.CharField(max_length=20)
    label_desc = models.CharField(max_length=40)

    class Meta:
        abstract = True


class CustomerLabel(LabelCode):
    class Meta:
        db_table = "Customer Label"
        verbose_name_plural = "Customer Label"


class EmployeeLabel(LabelCode):
    class Meta:
        db_table = "Employee Label"
        verbose_name_plural = "Employee Label"


class EmployeeStatus(StatusCode):
    class Meta:
        db_table = "EmployeeStatus"
        verbose_name_plural = "Employee Status"


class CustomerStatus(StatusCode):
    class Meta:
        db_table = "CustomerStatus"
        verbose_name_plural = "Customer Status"


class ProductStatus(StatusCode):
    class Meta:
        db_table = "ProductStatus"
        verbose_name_plural = "Product Status"


class StoreStatus(StatusCode):
    class Meta:
        db_table = "StoreStatus"
        verbose_name_plural = "Store Status"


class RewardStatus(StatusCode):
    class Meta:
        db_table = "RewardStatus"
        verbose_name_plural = "Reward Status"


class Country(models.Model):
    country_name = models.CharField(max_length=60)

    class Meta:
        db_table = "Country"
        verbose_name_plural = "Country"


class State(models.Model):
    state_name = models.CharField(max_length=60)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = "State"
        verbose_name_plural = "State/Province"


class Location(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=5)
    city = models.CharField(max_length=35)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "Location"
        verbose_name_plural = "Location/Address"


class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=14)
    comments = models.TextField(blank=True, null=True)
    birthdate = models.DateField()
    created_date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Employee(Person):
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "Employee"
        verbose_name_plural = "Employee"


class Customer(Person):
    create_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        db_table = "Customer"
        verbose_name_plural = "Loyalty Customer"


class Job(models.Model):
    job_name = models.CharField(max_length=40)
    job_desc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "Job"
        verbose_name_plural = "Job"


class EmployeeJob(models.Model):
    assign_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        db_table = "EmployeeJob"
        verbose_name_plural = "Employee Job"


class AssocEmployeeLabel(LabelCode):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employee_label = models.ForeignKey(EmployeeLabel, on_delete=models.CASCADE)

    class Meta:
        db_table = "AssocEmployeeLabel"
        verbose_name_plural = "Employee Label"


class AssocCustomerLabel(LabelCode):
    customer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer_label = models.ForeignKey(CustomerLabel, on_delete=models.CASCADE)

    class Meta:
        db_table = "AssocCustomerLabel"
        verbose_name_plural = "Customer Label"
