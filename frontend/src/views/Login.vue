<template>
  <div>
    <form class="login" @submit.prevent="login">
      <h1>Sign in</h1>

      <input v-model="username" id="username" class="input-box" type="text" placeholder="Username">
      <br>

      <input required v-model="password" class="input-box" type="password" placeholder="Password" >
      <div>
      <button type="submit">Login</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      message: 'Hello',
      username: '',
      password: '',
    };
  },
  mounted() {
    document.getElementById('username').focus();
  },
  methods: {
    login() {
      return 'OK';
    },
    updateTitle() {
      return new Date();
    },
  },
};
</script>

<style scoped>
  input {
    margin-top:10px;
  }
  input:focus {
    outline:0}
  button {
    margin-top:10px;
  }
  .input-box {
    width: 200px;
    border: 5px red;
    text-align:center;
  }
</style>
