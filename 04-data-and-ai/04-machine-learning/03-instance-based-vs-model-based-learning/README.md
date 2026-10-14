# Instance-Based vs Model-Based Learning

*Memorization vs. Generalization in Machine Learning*

**Instance-based learning** predicts by comparing a new example with stored training examples. **Model-based learning** predicts using a model that has learned patterns or relationships from the training data.

## 1. The Basic Idea

- **Instance-Based Learning:** relies heavily on individual training instances.
- **Model-Based Learning:** learns patterns from training data and creates a model that can generalize to unseen examples.

The key difference is how predictions are made.

## 2. Instance-Based Learning

In instance-based learning, the algorithm keeps training instances available and uses their similarity to a new example to make a prediction.

1. Receive a new data point.
2. Compare it with stored training examples.
3. Find the most similar or nearest examples.
4. Use those examples to make a prediction.

### Example: Student Pass/Fail

| Play Hours | Study Hours | Result |
|---:|---:|---|
| 8 | 1 | Fail |
| 7 | 2 | Fail |
| 6 | 2 | Fail |
| 2 | 8 | Pass |
| 3 | 7 | Pass |
| 1 | 9 | Pass |

For a new student with **6 play hours and 3 study hours**, an instance-based method checks which training students are most similar. If most relevant neighbors are labeled *Fail*, it predicts **Fail**.

The intuition is: **“Which existing examples look most like this one?”**

## 3. K-Nearest Neighbors (KNN)

K-Nearest Neighbors is a classic example of instance-based learning.

For a new point, KNN generally:
1. Calculates distances from training points.
2. Finds the nearest \(K\) points.
3. Uses their labels or values to predict.

For classification, the majority class among the nearest neighbors is commonly used. Euclidean distance is one possible distance measure.

## 4. Model-Based Learning

Model-based learning attempts to learn patterns or relationships from training data and represent them in a model.

1. Collect training data.
2. Learn patterns and model parameters.
3. Build a model.
4. Use the learned model to predict for new data.

Using the student example, a model may learn that **more study hours and fewer play hours are associated with a greater likelihood of passing**. Depending on the algorithm, the learned decision boundary could be linear, curved, or have another form.

The intuition is: **“What rule or pattern helps explain these examples?”**

## 5. Decision Boundaries and Generalization

A decision boundary separates regions predicted as different classes. After training, a model-based classifier uses its learned model to classify new points.

Instead of remembering only that one particular student failed, the model learns a relationship that can be applied to other students. This is the idea of **generalization**.

## 6. Memorization vs. Generalization

| Feature | Instance-Based Learning | Model-Based Learning |
|---|---|---|
| Main intuition | Remember and compare examples | Learn patterns and relationships |
| Training phase | Often stores examples; limited global model fitting | Learns model parameters or rules |
| Prediction | Uses similarity to stored instances | Uses the learned model |
| Training examples during prediction | Usually needed | Often not needed for ordinary prediction |
| Storage | Can be large because examples are retained | May be compact, depending on the model |
| Prediction speed | Can be slower for large datasets | Often faster after training |
| Example | KNN | Linear Regression, Logistic Regression, Decision Trees |

These are general tendencies, not universal rules. Costs depend on the algorithm, data representation, indexing, and model size.

## 7. Why Prediction Costs Can Differ

Suppose the training dataset contains one million records.

- **Model-based approach:** prediction may use a comparatively compact set of learned parameters.
- **Instance-based approach:** prediction may need to compare a new point with many stored examples to find useful neighbors.

Therefore, instance-based prediction can be more computationally expensive, especially when searching through a large training set without an efficient index.

## 8. Storage and Serialization

A trained model can often be serialized to a file, then loaded later for prediction. Python's `pickle` is one possible serialization format for suitable Python objects; some model libraries support their own formats.

For instance-based methods such as KNN, the stored training examples are usually part of what the fitted estimator needs to make predictions.

**Important:** Serialization is the process of saving an object or its state into a format that can later be reconstructed. It does not, by itself, mean that the saved artifact is small or independent of the training data.

## 9. One Important Nuance

The mnemonic **“instance-based = memorization; model-based = generalization”** is useful for an initial intuition, but it should not be taken literally.

Instance-based algorithms such as KNN can generalize to unseen examples. They do so by using similarity to stored examples rather than primarily by fitting a separate global model.

A precise distinction is:

- **Instance-based:** predict based on similarity to stored training instances.
- **Model-based:** predict using a learned model that captures patterns or relationships.

## 10. Quick Revision

| Concept | Key idea |
|---|---|
| Instance-based learning | Compare new examples with stored instances |
| KNN | Find nearest neighbors and use their labels/values |
| Model-based learning | Learn a model from the training data |
| Generalization | Apply learned relationships to unseen data |
| Decision boundary | Separates regions associated with different predicted classes |
| Serialization | Save an object/model so it can be loaded later |

## 11. Exam and Interview Questions

**Q1. What is instance-based learning?**  
An approach that predicts by comparing a new instance with stored training instances.

**Q2. Give an example of instance-based learning.**  
K-Nearest Neighbors (KNN).

**Q3. What is model-based learning?**  
An approach that learns patterns or relationships from training data and uses the resulting model for predictions.

**Q4. What is the key difference?**  
Instance-based learning relies on similarity to stored examples; model-based learning relies on a learned model.

**Q5. Which approach usually needs training instances at prediction time?**  
Instance-based learning.

**Q6. Why can model-based predictions be faster?**  
The prediction may use learned parameters directly rather than searching through many stored examples.

## Mental Model

- **Instance-Based:** `MEMORIZE EXAMPLES → COMPARE → PREDICT`
- **Model-Based:** `LEARN PATTERNS → GENERALIZE → PREDICT`

Remember: **“Which old examples look like this?”** versus **“What pattern did the model learn?”**
