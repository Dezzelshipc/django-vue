<template>
    <div></div>
</template>

<script>
export default {
    mounted() {
        localStorage.clear('usernameW')
        this.$router.push('/login')
    },
}
</script>