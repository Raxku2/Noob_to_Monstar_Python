import { h, Component } from 'preact'
import { useEffect,  useState } from 'preact/hooks';
const Menu = () => {
    const [docs, setDocs] = useState([]);
    const get_documents = async () => {
        const res = await fetch("http://localhost:8001/documents");
        const data = await res.json();
        setDocs(data);
    }

    useEffect(() => {
        get_documents();
    }, []);

    return (
        <div>
            <h1 hidden={docs} class="text-red-700 text-5xl">Loading</h1>
            {
                docs.map((doc) => {
                    // if (!doc)
                    return (

                        <div class="bg-white/4 p-4 border-2 my-2">
                            <h1>{doc.title}</h1>
                            <h4>{doc._id}</h4>
                        </div>
                    )
                })

            }

        </div>
    );
};

export default Menu;