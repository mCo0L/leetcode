class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Convert supplies to a set for O(1) lookups
        available = set(supplies)
        
        # Graph setup: in-degree and adjacency list
        indegree = {recipe: 0 for recipe in recipes}
        ingredient_to_recipe = {recipe: [] for recipe in recipes}
        
        # Build the graph
        for recipe, ing_list in zip(recipes, ingredients):
            for ing in ing_list:
                if ing not in available:  # If ingredient is not already in supplies
                    indegree[recipe] += 1  # Increase dependency count
                    ingredient_to_recipe.setdefault(ing, []).append(recipe)
        
        # Start with recipes that have zero in-degree (can be made immediately)
        queue = deque([r for r in recipes if indegree[r] == 0])
        result = []
        
        # Process the recipes in a topological order
        while queue:
            recipe = queue.popleft()
            result.append(recipe)
            available.add(recipe)  # Mark it as available
            
            # Reduce in-degree for dependent recipes
            for dependent in ingredient_to_recipe.get(recipe, []):
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        
        return result
        