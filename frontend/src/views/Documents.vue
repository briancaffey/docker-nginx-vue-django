<template>
  <div class="about">
    <h1>Documents in S3</h1>
    <div v-for="doc in documents" :key="doc.updated_at">
      <a :href="doc.upload">{{doc.upload}}</a>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Documents',
  data() {
    return {
      documents: [],
    };
  },
  mounted() {
    this.fetchDocuments();
    document.title = 'Documents';
  },
  methods: {
    fetchDocuments() {
      fetch('http://localhost:8000/api/posts/docs/all/', {
        method: 'GET',
        headers: {
          Accept: 'application/json',
        },
      }).then((response) => {
        if (response.ok) {
          response.json().then((json) => {
            this.documents = json;
          });
        }
      });
    },
  },
};

</script>
