# 🧠 Sorting Algorithms in Python

This project demonstrates the implementation and comparison of **Insertion Sort** and **Merge Sort** using Python.

You can take user input or test the algorithms on a predefined array.

## 📂 Files

- `main.py`: Main script that handles user interaction and runs both sorting algorithms.
- `insertion_sort.py`: Module containing the Insertion Sort algorithm.
- `merge_sort.py`: Module containing the Merge Sort algorithm.

---

## ▶️ How to Run

Make sure you have Python 3 installed. Then:

```bash
python main.py
```

You'll be prompted to:
1. Enter the size of the array.
2. Enter the elements one by one.
3. See the array sorted with both Merge Sort and Insertion Sort.

---

## 💻 Example

```
Enter the size of the array to be sorted: 5
Enter element 1: 9
Enter element 2: 3
Enter element 3: 7
Enter element 4: 1
Enter element 5: 5
```

Output:

```
The array received from the user:
9 3 7 1 5

Sorted with Merge Sort:
1 3 5 7 9

Sorted with Insertion Sort:
1 3 5 7 9
```

---

## 📈 Time Complexity

| Algorithm       | Best Case | Average Case | Worst Case |
|----------------|-----------|--------------|-------------|
| Insertion Sort | O(n)      | O(n²)        | O(n²)       |
| Merge Sort     | O(n log n)| O(n log n)   | O(n log n)  |



---

## 🛠 License

This project is open-source and available under the MIT License.
