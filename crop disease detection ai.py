import { useState } from "react";
import { Camera, Upload, ArrowUp, AlertCircle, CheckCircle } from "lucide-react";

export default function CropDoctor() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [result, setResult] = useState(null);
  
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedFile(file);
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };
  
  const analyzeImage = () => {
    if (!selectedFile) return;
    
    setAnalyzing(true);
    
    // Simulate analysis with timeout
    setTimeout(() => {
      // Mock disease detection result
      const diseases = [
        {
          name: "Leaf Blight",
          confidence: 92,
          description: "A fungal disease affecting the leaves, causing brownish lesions that expand rapidly.",
          treatment: "Apply copper-based fungicide every 7-10 days. Remove and destroy infected plant parts. Ensure proper spacing between plants for air circulation."
        }
      ];
      
      setResult({
        cropType: "Corn",
        diseases: diseases,
        overallHealth: "Poor",
        timeAnalyzed: new Date().toLocaleString()
      });
      
      setAnalyzing(false);
    }, 2000);
  };
  
  const resetForm = () => {
    setSelectedFile(null);
    setPreview(null);
    setResult(null);
  };
  
  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="bg-green-800 text-white p-4">
        <div className="container mx-auto flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="text-2xl font-bold flex items-center">
              <span className="text-green-300">
                <svg viewBox="0 0 24 24" width="24" height="24" className="mr-2">
                  <path fill="currentColor" d="M12,20C8.13,20 5,16.87 5,13C5,9.13 8.13,6 12,6C15.87,6 19,9.13 19,13C19,16.87 15.87,20 12,20M12,4C7.03,4 3,8.03 3,13C3,17.97 7.03,22 12,22C16.97,22 21,17.97 21,13C21,8.03 16.97,4 12,4M11,8H13V14H11V8M11,16H13V18H11V16Z" />
                </svg>
              </span>
              CropDoctor
            </div>
          </div>
          <nav>
            <ul className="flex gap-6">
              <li><a href="#" className="hover:text-green-200">About</a></li>
              <li><a href="#" className="hover:text-green-200">Help</a></li>
            </ul>
          </nav>
        </div>
      </header>
      
      {/* Main Content */}
      <main className="flex-grow bg-gray-50">
        <div className="container mx-auto py-8 px-4">
          <div className="text-center mb-8">
            <div className="flex justify-center mb-4">
              <div className="text-green-700">
                <svg viewBox="0 0 24 24" width="40" height="40">
                  <path fill="currentColor" d="M12,20C8.13,20 5,16.87 5,13C5,9.13 8.13,6 12,6C15.87,6 19,9.13 19,13C19,16.87 15.87,20 12,20M12,4C7.03,4 3,8.03 3,13C3,17.97 7.03,22 12,22C16.97,22 21,17.97 21,13C21,8.03 16.97,4 12,4M11,8H13V14H11V8M11,16H13V18H11V16Z" />
                </svg>
              </div>
            </div>
            <h1 className="text-4xl font-bold text-green-800 mb-2">Crop Disease Detection</h1>
            <p className="text-lg text-gray-600">
              Upload or capture an image of your crop to identify diseases and get treatment recommendations.
            </p>
          </div>
          
          <div className="max-w-3xl mx-auto bg-white rounded-lg shadow-md overflow-hidden">
            {!result ? (
              <div className="p-6">
                {!preview ? (
                  <>
                    <div className="flex flex-col md:flex-row gap-4 mb-6">
                      <label className="flex-1">
                        <div className="bg-green-500 hover:bg-green-600 text-white rounded-md p-4 flex items-center justify-center cursor-pointer">
                          <Upload className="mr-2" size={20} />
                          <span className="text-lg">Upload Image</span>
                        </div>
                        <input 
                          type="file"
                          className="hidden"
                          accept="image/*"
                          onChange={handleFileChange}
                        />
                      </label>
                      
                      <button className="flex-1 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-md p-4 flex items-center justify-center">
                        <Camera className="mr-2" size={20} />
                        <span className="text-lg">Use Camera</span>
                      </button>
                    </div>
                    
                    <div className="border-2 border-dashed border-green-300 rounded-lg p-8">
                      <div className="flex flex-col items-center justify-center text-gray-500">
                        <ArrowUp size={36} className="mb-3 text-gray-400" />
                        <p className="text-lg font-medium mb-1">Upload an image</p>
                        <p className="text-gray-500">Drag and drop an image here, or click to select a file</p>
                        <button className="mt-4 bg-green-500 hover:bg-green-600 text-white py-2 px-6 rounded-md">
                          Select Image
                        </button>
                      </div>
                    </div>
                  </>
                ) : (
                  <div>
                    <div className="mb-4">
                      <h3 className="text-lg font-semibold mb-2">Preview</h3>
                      <div className="aspect-video bg-gray-100 rounded flex items-center justify-center overflow-hidden">
                        <img 
                          src={preview} 
                          alt="Crop preview" 
                          className="max-w-full max-h-full object-contain"
                        />
                      </div>
                    </div>
                    
                    <div className="flex justify-between">
                      <button 
                        onClick={resetForm}
                        className="bg-gray-200 hover:bg-gray-300 text-gray-800 py-2 px-4 rounded"
                      >
                        Cancel
                      </button>
                      
                      <button 
                        onClick={analyzeImage}
                        className="bg-green-500 hover:bg-green-600 text-white py-2 px-6 rounded flex items-center"
                        disabled={analyzing}
                      >
                        {analyzing ? (
                          <>
                            <div className="animate-spin mr-2 h-5 w-5 border-2 border-white border-t-transparent rounded-full"></div>
                            Analyzing...
                          </>
                        ) : (
                          "Analyze Image"
                        )}
                      </button>
                    </div>
                  </div>
                )}
              </div>
            ) : (
              <div className="p-6">
                <div className="flex justify-between items-center mb-6">
                  <h2 className="text-2xl font-bold text-green-800">Analysis Results</h2>
                  <button 
                    onClick={resetForm} 
                    className="text-green-600 hover:text-green-800"
                  >
                    Analyze Another Image
                  </button>
                </div>
                
                <div className="grid md:grid-cols-5 gap-6">
                  <div className="md:col-span-2">
                    <div className="bg-gray-100 rounded p-2 flex items-center justify-center">
                      <img 
                        src={preview} 
                        alt="Analyzed crop" 
                        className="max-w-full max-h-64 object-contain"
                      />
                    </div>
                    
                    <div className="mt-4 bg-gray-50 rounded p-4">
                      <h3 className="font-medium mb-2">Image Information</h3>
                      <div className="text-sm">
                        <p className="flex justify-between py-1">
                          <span className="text-gray-600">Crop Type:</span>
                          <span className="font-medium">{result.cropType}</span>
                        </p>
                        <p className="flex justify-between py-1">
                          <span className="text-gray-600">Overall Health:</span>
                          <span className={`font-medium ${result.overallHealth === 'Poor' ? 'text-red-600' : 'text-green-600'}`}>
                            {result.overallHealth}
                          </span>
                        </p>
                        <p className="flex justify-between py-1">
                          <span className="text-gray-600">Analyzed:</span>
                          <span>{result.timeAnalyzed}</span>
                        </p>
                      </div>
                    </div>
                  </div>
                  
                  <div className="md:col-span-3">
                    <div className="mb-6">
                      <h3 className="text-xl font-semibold mb-3">Detected Diseases</h3>
                      
                      {result.diseases.map((disease, index) => (
                        <div key={index} className="mb-4 border-l-4 border-red-500 bg-red-50 p-4 rounded">
                          <div className="flex justify-between items-center mb-2">
                            <h4 className="text-lg font-medium flex items-center">
                              <AlertCircle size={18} className="text-red-500 mr-2" />
                              {disease.name}
                            </h4>
                            <span className="bg-red-100 text-red-800 text-sm py-1 px-2 rounded">
                              {disease.confidence}% Confidence
                            </span>
                          </div>
                          <p className="text-gray-700 mb-3">{disease.description}</p>
                        </div>
                      ))}
                    </div>
                    
                    <div>
                      <h3 className="text-xl font-semibold mb-3">Treatment Recommendations</h3>
                      
                      {result.diseases.map((disease, index) => (
                        <div key={index} className="mb-4 border-l-4 border-green-500 bg-green-50 p-4 rounded">
                          <h4 className="text-lg font-medium flex items-center mb-2">
                            <CheckCircle size={18} className="text-green-500 mr-2" />
                            For {disease.name}
                          </h4>
                          <p className="text-gray-700">{disease.treatment}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </main>
      
      {/* Footer */}
      <footer className="bg-green-800 text-white p-4 text-center">
        <p>&copy; Crop Disease Detection Tool</p>
      </footer>
    </div>
  );
}