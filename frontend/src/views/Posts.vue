<template>
  <div class="about">
    <h1>These are our posts!!</h1>
    <div v-for="post in posts" :key="post.id">
      <p>{{ post.title }}</p>
      <p>{{ post.content }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Posts',
  data() {
    return {
      posts: [],
    };
  },
  mounted() {
    this.fetchPosts();
    document.title = 'Posts';
  },
  methods: {
    fetchPosts() {
      fetch('http://localhost:8000/api/posts/', {
        method: 'GET',
        headers: {
          Accept: 'application/json',
        },
      }).then((response) => {
        if (response.ok) {
          response.json().then((json) => {
            this.posts = json;
          });
        }
      });
    },
  },
};

</script>
