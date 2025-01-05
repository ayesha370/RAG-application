<template>
  <div class="container">
    <!-- File Upload Section -->
    <div class="upload-container">
      <h2>Upload Document</h2>
      <input type="file" @change="handleFileUpload" id="fileInput" hidden />
      <button class="upload-btn" @click="triggerFileInput">Choose File</button>
      <p v-if="fileName" class="file-name">{{ fileName }}</p>
    </div>

    <!-- Query Input Section -->
    <div v-if="fileUploaded" class="query-container">
      <h2>Ask a Question</h2>
      <textarea
        v-model="query"
        class="query-box"
        placeholder="Ask a question about the document"
      ></textarea>
      <button class="ask-btn" @click="askQuestion" :disabled="!query">
        Ask
      </button>
    </div>

    <!-- Answer Display Section -->
    <div v-if="answer" class="answer-container">
      <h2>Answer</h2>
      <p class="answer-box">{{ answer }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      file: null,
      fileName: null,
      fileUploaded: false,
      query: '',
      answer: null,
    }
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0]
      this.fileName = this.file.name
      this.fileUploaded = true
    },
    triggerFileInput() {
      document.getElementById('fileInput').click()
    },
    async askQuestion() {
      try {
        // Simulate an API call for now
        this.answer = `You asked: "${this.query}". Here's the simulated response.`
      } catch (error) {
        console.error('Error processing the query:', error)
      }
    },
  },
}
</script>

<style scoped>
/* Main Container */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f9f9f9;
  font-family: Arial, sans-serif;
  padding: 20px;
}

/* Upload Section */
.upload-container {
  background: #ffffff;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  margin-bottom: 20px;
  width: 500px; /* Increased width */
}

.upload-btn {
  display: block;
  width: 100%;
  padding: 15px 0;
  margin: 10px 0;
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 18px; /* Increased font size */
  cursor: pointer;
}

.upload-btn:hover {
  background: #45a049;
}

.file-name {
  font-size: 16px; /* Increased font size */
  color: #666;
  margin-top: 10px;
}

/* Query Input Section */
.query-container {
  background: #ffffff;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  margin-bottom: 20px;
  width: 500px; /* Increased width */
}

.query-box {
  width: 100%;
  height: 100px; /* Increased height */
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 10px;
  resize: none;
  font-size: 16px; /* Increased font size */
}

.ask-btn {
  display: block;
  width: 100%;
  padding: 15px 0;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 18px; /* Increased font size */
  cursor: pointer;
}

.ask-btn:hover {
  background: #0056b3;
}

/* Answer Section */
.answer-container {
  background: #ffffff;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 500px; /* Increased width */
}

.answer-box {
  font-size: 16px; /* Increased font size */
  color: #333;
  text-align: left;
  word-wrap: break-word;
}
</style>
