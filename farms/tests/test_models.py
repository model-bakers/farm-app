from model_bakery import baker
from farms.models import Animal
import pytest


class TestFarm:
    def test_create_farm(self):
        # one way of importing a model: app_label.model_name
        farm = baker.prepare('farms.Farm')  # won't be persisted
        assert isinstance(farm.name, str)
        assert farm.area is not None

    def test_add_address_to_a_farm(self):
        # an example of OneToOne relation
        farm = baker.prepare('farms.Farm', _fill_optional=["address"])
        # returns a persisted address (see our docs)
        assert farm.address


class TestFarmer:
    def test_create_farmer_without_farm(self):
        # another way: ModelName
        farmer = baker.prepare('Farmer')
        assert isinstance(farmer.name, str)
        assert farmer.farm is None
        assert isinstance(farmer.age, int)

    def test_create_farmer_with_farm(self):
        farm = baker.prepare('farms.Farm')
        farmer = baker.prepare('Farmer', farm=farm)
        assert farmer.farm is not None


@pytest.mark.django_db  # needed because we are accessing the db with make
class TestAnimal:
    def test_create_cow(self):
        # another way: directly importing
        cow = baker.make(Animal, specie=Animal.Species.COW)  # using make will persist the object
        assert cow.specie == "COW"


@pytest.mark.django_db  # needed because we are accessing the db with make
class TestAddress:
    def test_create_addresses(self):
        addresses = baker.make('farms.Address', _quantity=5)

        assert len(addresses) == 5

    def test_create_address_with_optional_fields_filed(self):
        # this is a nice shortcut if you want all optional fields to be filed
        address = baker.make('farms.Address', _fill_optional=True)

        assert address.additional_info is not None

    def test_brazilian_farm(self):
        # creates an Address object random values for all fields, but country
        farm = baker.prepare('farms.Farm', address__country='Brazil')
        assert farm.address
        assert farm.address.country == 'Brazil'
