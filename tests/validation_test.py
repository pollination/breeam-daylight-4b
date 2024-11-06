from pollination.breeam_daylight_4b.entry import BreeamDaylight4bEntryPoint
from queenbee.recipe.dag import DAG


def test_breeam_daylight_4b():
    recipe = BreeamDaylight4bEntryPoint().queenbee
    assert recipe.name == 'breeam-daylight4b-entry-point'
    assert isinstance(recipe, DAG)
