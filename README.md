# 🛠️ Thread-Safe Producer-Consumer Queue 🧵🔄

Welcome to this **Bounded Blocking Queue** project! 🚀  
A classic **Producer-Consumer** model implemented in Python with full **thread safety** using locks and condition variables. Perfect for understanding the magic of multithreading and synchronization! 🧙‍♂️✨

---

## 🎯 Project Highlights

- ✅ **Thread-safe** queue with fixed capacity  
- 🔒 Uses `threading.Lock` and `threading.Condition` to ensure safe concurrent access  
- 🔄 Supports **multiple producers** and **multiple consumers** working simultaneously  
- 🚦 Automatically blocks producers if queue is full and consumers if queue is empty  
- 🐍 Written in clean, readable Python with detailed comments  

---

## 🧩 How It Works

- Producers call `put(item)` to add data; if full, they wait patiently ⏳  
- Consumers call `get()` to retrieve data; if empty, they wait for producers to supply 🍽️  
- Synchronization primitives manage access, avoiding race conditions and deadlocks ⚔️  

---

## 🧑‍💻 Example Output Snippet
Producer 1 produced: 0
Consumer 1 consumed: 0
Producer 2 produced: 10
Consumer 2 consumed: 10
...
All producers and consumers have finished.

---

## 🚀 Future Ideas

- Add timeout support ⏰ for `put()` and `get()`  
- Implement an asynchronous version using `asyncio` ⚡  
- Benchmark performance under different workloads 📊  
- Wrap it into a reusable Python package 📦  

---

## 🤝 About the Author

Shuai Qian （Alex Quinn）  
Passionate about data structures, algorithms, and system programming. Always learning, always coding! 💡💻

---

Feel free to ⭐ star this repo if you find it useful or interesting!

---

Happy coding! 🎉🐍

