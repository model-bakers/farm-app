from model_bakery import baker
from farms.models import Animal
import pytest


class TestFarm:
    def test_create_farm(self):
        # one way of importing a model: app_label.model_name
        farm = baker.prepare('farms.Farm')  # won't be persisted
        assert isinstance(farm.name, str)
        assert isinstance(farm.address, str)
        assert farm.area is not None


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
