<template>
  <div id="app">
    <h1>RAG App - Document Upload & Query System</h1>
    <DocumentUpload />
  </div>
</template>

<script>
import DocumentUpload from './components/DocumentUpload.vue';

export default {
  components: {
    DocumentUpload,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
</style>
