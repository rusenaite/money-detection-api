import { useState } from "react";
import axios from "axios";

function App() {
    const [image, setImage] = useState(null);
    const [result, setResult] = useState(null);
    const [preview, setPreview] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setImage(file);
            setPreview(URL.createObjectURL(file)); // Show preview of uploaded image
            setError(null);
        }
    };

    const handleUpload = async () => {
        if (!image) {
            setError("Please select a file before uploading.");
            return;
        }

        const formData = new FormData();
        formData.append("image", image);
        setLoading(true);
        setError(null);

        try {
            const response = await axios.post("http://127.0.0.1:8000/upload/", formData, {
                headers: { "Content-Type": "multipart/form-data" },
            });

            if (response.data.processed) {
                setResult(response.data);
            } else {
                setError("Processed image not received from the server.");
            }
        } catch (error) {
            setError("Error uploading the image. Please check the server.");
            console.error("Error:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ textAlign: "center", padding: "20px", fontFamily: "Arial, sans-serif" }}>
            <h1>Image Processing</h1>

            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload} style={{ marginLeft: "10px", padding: "8px 16px" }} disabled={loading}>
                {loading ? "Uploading..." : "Upload"}
            </button>

            {error && <p style={{ color: "red", marginTop: "10px" }}>{error}</p>}

            {/* Image Display Section */}
            <div style={{ display: "flex", justifyContent: "center", gap: "20px", marginTop: "20px" }}>
                {preview && (
                    <div>
                        <h3>Original Image</h3>
                        <img src={preview} alt="Original" style={{ width: "300px", border: "1px solid #ddd", borderRadius: "8px" }} />
                    </div>
                )}

                {result && result.processed && (
                    <div>
                        <h3>Processed Image</h3>
                        <img src={result.processed} alt="Processed" style={{ width: "300px", border: "1px solid #ddd", borderRadius: "8px" }} />
                    </div>
                )}
            </div>
        </div>
    );
}

export default App;
