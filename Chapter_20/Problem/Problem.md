# Practice Set – Chapter 20 (HTTP Requests)

1. Write a Python script to fetch your public IP using `https://httpbin.org/ip`.  
2. Send a GET request to `https://httpbin.org/get` with parameters: `{ "course": "python", "level": "beginner" }`.  
3. Make a POST request to `https://httpbin.org/post` with JSON data: `{ "id": 1, "task": "Learn requests" }`.  
4. Add a custom header `X-Student: YourName` in a GET request.  
5. Try to access `https://httpbin.org/status/500` and handle the error gracefully.  
6. Write a script that fetches the first 5 users from `https://jsonplaceholder.typicode.com/users`.  
7. Send a POST request with form data instead of JSON.  
8. Create a reusable function `fetch_data(url)` that returns JSON data or error.  
9. Implement basic authentication in a request (`https://httpbin.org/basic-auth/user/pass`).  
10. Fetch your GitHub user profile data using `https://api.github.com/users/<your-username>`.  
