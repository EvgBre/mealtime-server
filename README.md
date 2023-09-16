# MealTime Client

MealTime is a new digital platform for anyone that needs a way to organize and incorporate meal planing into their daily routine! The app provides a basic catalog for someone to add any food of their choice, combine those foods into meals, and plan out when they want to have them throughout the week.
Built to make your grocery shopping AND eating lifestyle easier, MealTime is the perfect virtual solution! 

## App Users <!-- This is a scaled down user persona -->
- Anyone that wants to create a disciplined way of organizing a meal prep plan on a week-by-week basis.
- Athletes that want to build meals around that routine so they can track the amount of grams being consumed on the days that they workout or rest.
- People that are trying to change their eating lifestyle, and want to track their grams per meal and view all my created foods by type.
- Anyone that wants to prep a food list for grocery shopping. If they schedule when they have certain meals, they can easily make a weekly grocery list.

## Features <!-- List your app features using bullets! Do NOT use a paragraph. No one will read that! -->
- MealTime uses Google authentication for users to log in before adding their personal information, including their preferred diet.
- As a user, you can create as many food items and meals as you desire.
- Users have a food page showing items on their list, where they can add more via a modal or delete them from the food card. 
- Users also have a meal page showing all the meals they have created. The meal cards can direct them to the meal details page, route them to a form for editing, or delete them.
- On the individual meal detail pages, a user can add foods to that specific meal and add how many grams they want. This will create a separate food card displaying the food name, type, and grams.
- Once added to a meal, a food can be removed at any time without deleteing the actual food item from the users food list.
- Users can view all meals in order of the calendar date they created it with.
- Users can only see the foods and meals that they created.


## Relevant Links <!-- Link to all the things that are required outside of the ones that have their own section -->
- [ERD](https://dbdiagram.io/d/64dab2db02bd1c4a5ec5752e)
- [Wireframes](https://www.figma.com/file/Eebb7ycjEUCTXMoZrNtSWd/MealTime-Wireframe?type=design&node-id=0-1&mode=design&t=da3tNYD4ww0ZTrCo-0)
- [Project Board](https://github.com/users/EvgBre/projects/3)
- [Server-side Repository](https://github.com/EvgBre/mealtime-server/tree/main)


## Code Snippet <!-- OPTIONAL, but doesn't hurt -->
```
  const handleSubmit = (e) => {
    // Prevent form from being submitted
    e.preventDefault();

    const food = {
      foodId: formInput.food_id,
      mealId: id,
      grams: formInput.grams,
    };
      // Send POST request to your API
    createMealFood(food).then(() => {
      onUpdate();
    });
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormInput((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Dialog>
        <Modal.Header closeButton>
          <Modal.Title>Add a Food Item to this Meal!</Modal.Title>
        </Modal.Header>

        <Modal.Body>
          <Form onSubmit={handleSubmit}>

            <Form.Group className="mb-3">
              <Form.Label>Food Select</Form.Label>
              <Form.Select
                aria-label="Food"
                name="food_id"
                onChange={handleChange}
                className="mb-3"
                value={formInput.food_id}
                required
              >
                <option value="">Select a Food</option>
                {
            foods.map((food) => (
              <option
                key={food.id}
                value={food.id}
              >
                {food.name}
              </option>
            ))
          }
              </Form.Select>
            </Form.Group>
            <Form.Group className="mb-2">
              <Form.Label>How many grams of this food are you having?</Form.Label>
              <Form.Control
                name="grams"
                required
                value={formInput.grams}
                type="number"
                onChange={handleChange}
              />
            </Form.Group>

            <Button variant="dark" type="submit">
              Submit
            </Button>
          </Form>

        </Modal.Body>
      </Modal.Dialog>
    </Modal>
  );
```

## Project Screenshots <!-- These can be inside of your project. Look at the repos from class and see how the images are included in the readme -->
- TBA

## Video Walkthrough
- TBA


## Contributors
- [Evan Breland](https://github.com/EvgBre)
