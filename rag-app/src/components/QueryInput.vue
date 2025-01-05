<template>
  <div>
    <h2>Ask a Question</h2>
    <input v-model="query" placeholder="Ask a question about the document" />
    <button @click="askQuestion" :disabled="!query">Ask</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: '',
    }
  },
  methods: {
    async askQuestion() {
      try {
        const response = await this.$axios.post(
          'http://localhost:8000/query/',
          {
            query: this.query,
            document_id: 1, // Use the actual document ID after uploading
          }
        )
        this.$emit('answer-received', response.data.answer)
      } catch (error) {
        console.error('Error fetching answer:', error)
      }
    },
  },
}
</script>

<style scoped>
button {
  margin-top: 10px;
}
</style>
