````md
# PDC_Coursework – Chapter 6 Experiments

This project contains practical experiments demonstrating **distributed and network-based programming concepts** using **Pyro4 (Python Remote Objects)**, **Celery (distributed task queue)**, and **Python socket programming**.  
Each section below summarizes the execution steps, observed outputs, and conclusions for the respective experiments.

---

## 1. Pyro4 – Simple Server–Client Example

### Files
- `pyro_server.py`
- `pyro_client.py`

### Procedure & Observations

#### Start the Pyro Name Server
```bash
python -m Pyro4.naming
````

**Output:**

```
NS running on localhost:9090 (127.0.0.1)
Warning: HMAC key not set. Anyone can connect to this server!
URI = PYRO:Pyro.NameServer@localhost:9090
```

* The name server starts successfully on port **9090**.
* The HMAC warning indicates that authentication is disabled, which is acceptable for local testing.

#### Start the Pyro Server

```bash
python pyro_server.py
```

**Output:**

```
Ready. Object uri = PYRO:obj_3908a1f7ca7546238bfb6ad879e148f0@localhost:59945
```

* The server registers itself with the Pyro name server.
* It is now ready to handle incoming client requests.

#### Run the Client

```bash
python pyro_client.py
```

* The client prompts the user for a name.
* A welcome message is received from the remote server.

### Conclusion

The basic Pyro4 server–client setup works correctly. The client successfully locates the server via the name server and executes remote methods using the object URI.

---

## 2. Pyro4 – Chain of Servers Example

### Files

* `server_chain_1.py`
* `server_chain_2.py`
* `server_chain_3.py`
* `client_chain.py`

### Observed Outputs

**Server 1**

```
server_1 started
1 forwarding the message to the object 2
Back at 1; the chain is closed!
```

**Server 2**

```
server_2 started
2 forwarding the message to the object 3
```

**Server 3**

```
server_3 started
3 forwarding the message to the object 1
```

**Client**

```
Result = ['passed on from 1', 'passed on from 2', 'passed on from 3', 'complete at 1']
```

### Analysis

* The servers form a **cyclic chain**:
  **Server 1 → Server 2 → Server 3 → Server 1**
* Each server forwards the request to the next server in the chain.
* The client receives a complete list of messages confirming the traversal order and successful completion.

### Conclusion

The chained Pyro4 server example operates as intended, demonstrating remote method invocation across multiple interconnected servers.

---

## 3. Celery – Add Task Example

### Files

* `addTask.py`
* `addTask_main.py`

### Execution Steps

#### Start the Celery Worker

```bash
celery -A addTask worker --loglevel=info
```

**Expected Worker Output:**

```
[INFO/MainProcess] Connected to amqp://guest@localhost//
[INFO/MainProcess] mingle: searching for neighbors
[INFO/MainProcess] mingle: all alone
[INFO/MainProcess] celery@hostname ready.
```

#### Execute the Task

```python
add.delay(5, 5)
```

**Worker Output:**

```
[INFO/MainProcess] Received task: addTask.add[]
[INFO/MainProcess] Task addTask.add[] succeeded in 0.001s: 10
```

### Conclusion

The Celery task executes successfully. The distributed worker processes the task and returns the correct result (`10`) for `add(5,5)`.

---

## 4. Socket Programming Examples

### Files

* `server2.py`
* `client2.py`
* `client.py`

---

### 4.1 Simple Time Client (`client.py`)

**Client Code Overview**

* Establishes a TCP socket connection.
* Connects to the server on port **9999**.
* Receives and prints the server’s current time.

**Observed Output**

```
Time connection server: Wed Dec 24 03:19:37 2025
```

### Conclusion

The client successfully connects to the server and retrieves the current time, demonstrating basic TCP communication.

---

### 4.2 File Transfer Client (`client2.py`)

#### Initial Issue

The server failed to locate the source file:

```
FileNotFoundError: [Errno 2] No such file or directory: 'mytext.txt'
```

#### After Fix

Once `mytext.txt` was placed in the server directory:

```
file opened
receiving data...
Successfully get the file
connection closed
```

### Conclusion

The file transfer example works correctly when the required file exists on the server. The initial error highlights the importance of proper file handling on the server side.

---

## Overall Summary

| Experiment             | Status  | Remarks                                               |
| ---------------------- | ------- | ----------------------------------------------------- |
| Pyro4 – Simple Example | ✅ Works | Successful client–server communication via Pyro4      |
| Pyro4 – Chain Example  | ✅ Works | Messages propagate correctly through server chain     |
| Celery Add Task        | ✅ Works | Distributed task executes and returns expected result |
| Socket File Transfer   | ⚠ Fixed | Fails without source file; works once file exists     |
| Socket Time Client     | ✅ Works | Simple TCP connection retrieves server time           |

---

## Final Remarks

All experiments demonstrate their intended concepts effectively. Pyro4 showcases remote object communication, Celery highlights distributed task processing, and socket programming illustrates low-level client–server communication and file transfer mechanisms.

```
```