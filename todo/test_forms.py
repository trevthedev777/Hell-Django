from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())  # to see if there is a 'name' key in the dictionary form_errors  # noqa
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_required(self):
        form = ItemForm({'name': ' Test Todo Item'})
        self.assertTrue(form.is_valid())

    # checks that no extra form fields are included if the model is updated
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
