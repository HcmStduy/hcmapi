<template>
    <div class="ok">
        {{msg}}
        <div>
            <swiper></swiper>
            <swiper></swiper>
            <swiper></swiper>
            <swiper></swiper>
            <swiper></swiper>
        </div>

    </div>

</template>

<script>
    import swiper from "@/components/swiper.vue";
    export default {
        name: "Me",
        components: {swiper},
        data: ()=>{
            return {
                msg :'个人中心'
            }
        },

    }
</script>

<style scoped>
    .ok{
        color: red;
        font-size: 50px;
    }
</style>