import { h, Component } from 'preact';
import { useEffect, useState } from 'preact/hooks';

import { marked } from 'https://cdn.jsdelivr.net/npm/marked/+esm';

const Editor = () => {
    const [text, setText] = useState('');
    const [markedTest, setMarkedText] = useState("");

    const get_doc = async (doc_id) => {
        const res = await fetch(`http://localhost:8001/doc?doc_id=${doc_id}`);
        const data = await res.json();
        setText(data.doc);
    }

    const create_doc = async () => {
        const title = prompt("enter doc title")
        const res = await fetch(`http://localhost:8001/doc`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "title": title,
                "data": text
            })
        });
        // const data = await res.json();
        if (res.status == 201){
            alert("Document created")
        }
    }

    useEffect(() => {
        setMarkedText(marked.parse(text));

    }, [text])

    return (
        <div>
            this is editor
            <div class="w-full flex">

                <textarea name="" id="" class="h-90 w-[50%] bg-white/4 p-2"
                    value={text}
                    onInput={(e) => {
                        setText(e.target.value);
                    }}
                ></textarea>
                <div class="w-[50%] bg-white/4 border-l-2 h-90 p-2 overflow-x-hidden overflow-y-scroll "
                    id='preview'
                    dangerouslySetInnerHTML={{ __html: markedTest }}
                >

                </div>


            </div>

            <div>
                <button class="m-1 p-2 border-2 rounded-lg"
                    onClick={() => {
                        const doc_id = prompt("enter document id ");
                        get_doc(doc_id);

                    }}>
                    Open
                </button>
                <button class="m-1 p-2 border-2 rounded-lg"
                    onClick={() => {
                        create_doc();
                    }}>
                    save
                </button>

            </div >

        </div >
    );
};

export default Editor;