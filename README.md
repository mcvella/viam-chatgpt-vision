# ChatGPT modular vision service

This module implements the [rdk vision API](https://github.com/rdk/vision-api) in a mcvella:vision:chatgpt model.

This model leverages [OpenAI's ChatGPT](chatgpt.com) model gpt-4o to allow for image classification and querying.
OpenAI API access is required, so you must register for an account and create [project API key](https://platform.openai.com/api-keys)

## Build and Run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the `mcvella:vision:chatgpt` model from the [mcvella chatgpt-vision module](https://app.viam.com/module/mcvella/chatgpt-vision).

## Configure your vision service

> [!NOTE]  
> Before configuring your vision service, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

Navigate to the **Config** tab of your robot’s page in [the Viam app](https://app.viam.com/).
Click on the **Service** subtab and click **Create service**.
Select the `vision` type, then select the `mcvella:vision:chatgpt` model.
Enter a name for your vision service and click **Create**.

On the new service panel, copy and paste the following attribute template into your vision service's **Attributes** box:

```json
{
  "api_key": "<OpenAI api key>",
  "default_question": "describe this image"
}
```

> [!NOTE]  
> For more information, see [Configure a Robot](https://docs.viam.com/manage/configuration/).

### Attributes

The following attributes are available for `mcvella:vision:chatgpt` model:

| Name | Type | Inclusion | Description |
| ---- | ---- | --------- | ----------- |
| `api_key` | string | **Required** |  OpenAI API key |
| `default_question` | string | |  Default question, can be overridden via extra in classification request |

### Example Configurations

```json
{
  "api_key": "abc123"
}
```

## API

The chatgpt-vision resource provides the following methods from Viam's built-in [rdk:service:vision API](https://python.viam.dev/autoapi/viam/services/vision/client/index.html)

### get_classifications(image=*binary*, count)

### get_classifications_from_camera(camera_name=*string*, count)

Note: if using this method, any cameras you are using must be set in the `depends_on` array for the service configuration, for example:

```json
      "depends_on": [
        "cam"
      ]
```

By default, the chatgpt-vision model will be asked the question "describe this image".
If you want to ask a different question about the image, you can pass that question as the extra parameter "question".
For example:

``` python
chatgpt.get_classifications(image, 1, extra={"question": "what is the person wearing?"})
```
