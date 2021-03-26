<!--- Provide a general summary of your changes in the Title above. -->

<!--- Title format: `<type>[optional scope]: [STORY ID#]<description> -->
<!--- Possible types: feat|fix|chore|build|test|perf|refactor -->
<!--- Optional scopes: (WHEN USING THIS TEMPLATE PLEASE ADD SOME SCOPES LIKE USECASES ECT.) -->

### Description
<!--- Describe your changes in detail -->

### Motivation and Context
<!--- Why is this change required? What problem does it solve? -->
<!--- If it fixes an open issue, please add [STORY ID#] in the subject -->

### How Has This Been Tested?
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->

### Types of changes
<!--- What types of changes does your code introduce? Put an `x` in all the boxes that apply: -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (breaks existing functionality to add fix / feature) if yes add BREAKING CHANGE <description> to the PR body.

### Checklist
<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask.-->
- [ ] My change requires a change to the documentation.
- [ ] I have added tests to cover my changes.
- [ ] My change causes a model performance change 


### Common Style and Readability Checks
<!--- Please go though each of these checks and consider if your changes comply with them -->
<!--- If you're unsure about any of these speak with your teammates/reviewers as they can help you.-->
- [ ] Code has clear descriptive naming for variables. Example temp vs temperature
- [ ] Code has clear, descriptive, and accurate naming for methods and their arguments
- [ ] No uncommon abbreviation
- [ ] State is kept as local as possible
- [ ] Logic branching complexity is kept to a minimum
- [ ] Code is not repeated
- [ ] Side effects are kept to a minimum
- [ ] Flow of logic can be followed all the way through
- [ ] Complexity is at an appropriate level for the problem
- [ ] Complies with company style standards


### Data Checks
<!--- Please go though each of these checks and consider if your changes comply with them -->
<!--- If you're unsure about any of these speak with your teammates/reviewers as they can help you.-->
- [ ] Do we have notes on the meanings of the columns and tables we are pulling from the client?
- [ ] Joins are done correctly. The number of rows matches expectations, no duplicate columns, etc.
- [ ] Duplicate date points are handled appropriately


### Machine Learning Specific Checks
<!--- Please go though each of these checks and consider if your changes comply with them -->
<!--- If you're unsure about any of these speak with your teammates/reviewers as they can help you.-->
- [ ] No Target Leakage
- [ ] Aggregate features only use information from their own past. E.g. no future information
- [ ] Over fitting is tested for
- [ ] Train and test splits are representative
- [ ] Model hyper parameters are reasonable for the problem
- [ ] The number of iterations for the problem is not so high as to invite the multiple comparisons problem https://www.stat.berkeley.edu/~mgoldman/Section0402.pdf
- [ ] No static date features. E.g the year.
- [ ] A realistic and customer relevant evaluation metric is used. Example $s saved 
- [ ] Feature importance checks have been done
- [ ] A reasonable baseline for comparison is used
- [ ] The complexity of the model is matched to the complexity of the problem and the dataset
- [ ] Missing values are handled in a reasonable manner
- [ ] Changes to the pipeline have been validated by checking instances
