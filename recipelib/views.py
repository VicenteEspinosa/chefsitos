from django.shortcuts import render

from recipelib.api_views.ingredient import IngredientView
from recipelib.api_views.measurement import MeasurementView
from recipelib.api_views.recipe import (
    FeedView,
    RateRecipeView,
    RecipeView,
    SelfRecipesView,
)
from recipelib.api_views.tag import TagView
from recipelib.api_views.user import (
    UserFollow,
    UserSignin,
    UserSignout,
    UserSignup,
    UserView,
)
