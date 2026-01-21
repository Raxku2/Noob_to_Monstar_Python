import { useState } from 'preact/hooks'
import Router, { route } from 'preact-router'
import { Editor, Menu } from './components';
export function App() {
  const [count, setCount] = useState(0);



  return (
    <>
      <Router>
        <div path="/">
          Home page
        </div>
        <Editor path="editor" />
        <Menu path="/menu" />
      </Router>
      <div class=" ">
        <button class="m-1 p-2 border-2 rounded-lg"
          onClick={() => {
            route('/menu')
          }}>
          Menu
        </button >
        <button class="m-1 p-2 border-2 rounded-lg"
          onClick={() => {
            route('/editor')
          }}>
          Editor
        </button>
        <button class="m-1 p-2 border-2 rounded-lg"
          onClick={() => {
            route('/')
          }}>
          Home
        </button>

      </div>
    </>
  )
}
