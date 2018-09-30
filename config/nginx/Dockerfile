FROM node:8.12.0-alpine as build-stage
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY . .
RUN cd frontend && npm run build

# production stage
FROM nginx:1.13.12-alpine as production-stage
COPY --from=build-stage /app/frontend/dist /usr/share/nginx/html
# COPY frontend/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
