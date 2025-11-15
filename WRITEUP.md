### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

  
  I chose App Service because it is fully managed, scales automatically with traffic, and reduces maintenance costs compared to a VM. The workflow is simpler, and it allows us to deploy Python apps directly from local or GitHub without managing OS or web server manually.
  
### Assess app changes that would change your decision.
Since I have deployed  Python CMS app on Azure App Service, it changes how we manage and run the app in a few ways:
Less control over the server
Unlike a VM, we don’t have full access to the operating system or server settings. This means we can’t install custom software or tweak low-level settings. On the plus side, it makes maintenance much simpler.

Easier deployment workflow

App Service lets us deploy directly from our local machine, GitHub, or Azure DevOps. We don’t need to worry about patching or updating the server—it’s all handled automatically.

Additional Adjustments Needed

Environment variables

All sensitive info like the database credentials, storage keys, and secret keys must be set in App Service → Configuration. We can’t rely on local .env files anymore.

Storage access

Images must be uploaded to Azure Blob Storage because App Service is stateless. The app has to generate correct URLs, and the storage container must allow public access.

Logging and monitoring

Since the app runs in the cloud, we rely on Log Stream and Application Insights to track successful and failed login attempts.

File uploads

Temporary storage on App Service is limited, so all uploads (like images) need to go straight to Blob Storage instead of the local server.
